document.querySelector('#mediaDev').addEventListener('click', mediaDev)
document.querySelector('#createRoom').addEventListener('click', createRoom)
document.querySelector('#joinRoom').addEventListener('click', joinRoom)
const msg = document.querySelector('#msg')

let configuration = {iceServers: [{urls: 'stun:stun.l.google.com:19302'}],iceCandidatePoolSize: 10}
let peerConnection = null;
let localStream = null;
let remoteStream = null;
let roomDialog = null;
let roomId = null;

async function mediaDev(){
  document.querySelector('#mediaDev').hidden = true;
  document.querySelector('#createRoom').hidden = false;
  document.querySelector('#joinRoom').hidden = false;
  const localPlayback = document.querySelector('#localAudio')
  const remotePlayback = document.querySelector('#remoteAudio')

  localStream = await navigator.mediaDevices.getUserMedia({'video': false, 'audio': true});
  remoteStream = new MediaStream();
  localPlayback.srcObject = localStream;
  remotePlayback.srcObject = remoteStream;
}

async function createRoom(){
  document.querySelector('#createRoom').hidden = true;
  document.querySelector('#joinRoom').hidden = true;
  
  const db = firebase.firestore();
  const roomRef = await db.collection('rooms').doc();
  peerConnection = new RTCPeerConnection(configuration);


  localStream.getTracks().forEach(track => {
    peerConnection.addTrack(track, localStream);
  });
  peerConnection.addEventListener('track', event => {
    console.log('Got remote track:', event.streams[0]);
    event.streams[0].getTracks().forEach(track => {
      console.log('Add a track to the remoteStream:', track);
      remoteStream.addTrack(track);
    });
  });

  const callerCandidatesCollection = roomRef.collection('callerCandidates');
  peerConnection.addEventListener('icecandidate', event => {
    if (!event.candidate) {
      console.log('Got final candidate!');
      return;
    }
    console.log('Got candidate: ', event.candidate);
    callerCandidatesCollection.add(event.candidate.toJSON());
  });


  const offer = await peerConnection.createOffer();
  await peerConnection.setLocalDescription(offer);
  await roomRef.set({'offer': {type: offer.type, sdp: offer.sdp}});
  roomId = roomRef.id;
  msg.innerText = `Current room is ${roomRef.id} - You are the caller!`;


  roomRef.onSnapshot(async snapshot => {
    const data = snapshot.data();
    if (!peerConnection.currentRemoteDescription && data && data.answer) {
      console.log('Got remote description: ', data.answer);
      const rtcSessionDescription = new RTCSessionDescription(data.answer);
      await peerConnection.setRemoteDescription(rtcSessionDescription);
    }
  });

  roomRef.collection('calleeCandidates').onSnapshot(snapshot => {
    snapshot.docChanges().forEach(async change => {
      if (change.type === 'added') {
        let data = change.doc.data();
        console.log(`Got new remote ICE candidate: ${JSON.stringify(data)}`);
        await peerConnection.addIceCandidate(new RTCIceCandidate(data));
      }
    });
  });

}

function joinRoom(){
  document.querySelector('#createRoom').hidden = true;
  document.querySelector('#joinRoom').hidden = true;
  document.querySelector('#joinDiv').hidden = false;
  
  document.querySelector('#joinButton').addEventListener('click', async () => {
    roomId = document.querySelector('#room-id').value;
    msg.innerText = `(Returner) The room id: ${roomId}`;
    await joinRoomID(roomId);
  }, {once: true});
}

async function joinRoomID(roomId){
  const db = firebase.firestore();
  const roomRef = db.collection('rooms').doc(`${roomId}`);
  const roomSnapshot = await roomRef.get();
  console.log('Got room:', roomSnapshot.exists);

  if (roomSnapshot.exists) {
    console.log('Create PeerConnection with configuration: ', configuration);
    peerConnection = new RTCPeerConnection(configuration);


    localStream.getTracks().forEach(track => {
      peerConnection.addTrack(track, localStream);
    });
    peerConnection.addEventListener('track', event => {
      console.log('Got remote track:', event.streams[0]);
      event.streams[0].getTracks().forEach(track => {
        console.log('Add a track to the remoteStream:', track);
        remoteStream.addTrack(track);
      });
    });


    const calleeCandidatesCollection = roomRef.collection('calleeCandidates');
    peerConnection.addEventListener('icecandidate', event => {
      if (!event.candidate) {
        console.log('Got final candidate!');
        return;
      }
      console.log('Got candidate: ', event.candidate);
      calleeCandidatesCollection.add(event.candidate.toJSON());
    });



    const offer = roomSnapshot.data().offer;
    console.log('Got offer:', offer);
    await peerConnection.setRemoteDescription(new RTCSessionDescription(offer));
    const answer = await peerConnection.createAnswer();
    console.log('Created answer:', answer);
    await peerConnection.setLocalDescription(answer);
    await roomRef.update({answer: {type: answer.type, sdp: answer.sdp}});


    roomRef.collection('callerCandidates').onSnapshot(snapshot => {
      snapshot.docChanges().forEach(async change => {
        if (change.type === 'added') {
          let data = change.doc.data();
          console.log(`Got new remote ICE candidate: ${JSON.stringify(data)}`);
          await peerConnection.addIceCandidate(new RTCIceCandidate(data));
        }
      });
    });
  }
}

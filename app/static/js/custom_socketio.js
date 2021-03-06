document.addEventListener('DOMContentLoaded',()=>{
    let socket = io.connect('http://'+ document.domain + ':' + location.port);
    
    const username = document.querySelector('#get-username').innerHTML;

    let room = "lounge";
    joinRoom("lounge")


      socket.on('message', data =>{
        const p = document.createElement('p');
        const span_username = document.createElement('span');
        const span_timestamp = document.createElement('span');
        const br = document.createElement('br');

        if(data.username){
            span_username.innerHTML = data.username;
            span_timestamp.innerHTML = data.time_stamp;

            if(data.username === username){
                p.classList.add('my-msg');
                span_username.classList.add('my-username');
            } else {
                p.classList.add('others-msg');
                span_username.classList.add('other-username');
            }
            span_timestamp.classList.add('timestamp');

            p.innerHTML = span_username.outerHTML + span_timestamp.outerHTML +br.outerHTML + data.msg 
                + br.outerHTML ;
            

            document.querySelector("#display-message-section").append(p)

            const display_msg = document.querySelector('#display-message-section')
            showNewMessage(display_msg); // scroll up for the latest message


        } else {
            printSysMsg(data.msg);
        }
        

    })

    document.querySelector("#send_message").onclick = ()=>{
        const the_message = document.querySelector("#user_message").value;
        if(the_message === ""){
            document.querySelector("#user_message").focus();
        }
        else{
            socket.send({'msg': the_message,
            'username': username, 'room': room });
            document.querySelector("#user_message").value = '';
        }
    }

    document.querySelectorAll('.select-room').forEach(p =>{
        p.onclick = () =>{
            let newRoom = p.innerHTML;
            if (newRoom == room){
                msg = `You are already in ${room} room.`
                printSysMsg(msg);
            } else {
                leaveRoom(room);
                joinRoom(newRoom);
                room = newRoom;
            }

        }
    })

   
    function showNewMessage(node){
        node.scrollTop = node.scrollHeight
    }

    function leaveRoom(room){
        socket.emit('leave',{'username': username, 'room':room})
    }

    function joinRoom(room){
        socket.emit('join',{'username': username, 'room':room})
        document.querySelector('#display-message-section').innerHTML = ''
    }
    
    function printSysMsg(msg){
        const p = document.createElement('p');
        p.innerHTML = msg;
        p.classList.add('system-msg');
        document.querySelector('#display-message-section').append(p);
    }
})
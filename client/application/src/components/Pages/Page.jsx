import React, { useEffect, useState } from "react";
import { Toast } from "react-bootstrap";

import Header from "./Header";
import Content from "./Content"
import Footer from "./Footer";

import "./Page.css"

export default function Page() {

    const [ state, setState ] = useState({
        message : "Hello",
        toastInfo : {
                status : "info",
                title : "Toast Title",
                message : "This is a toast message!"
            },
        showToast : false,
        internetConnection : true
    })

    const callbackConnect = () => {
        // console.log("Internet Conected")
        setState({
            ...state,
            showToast : false,
            internetConnection : true,
            toastInfo : {
                title : "",
                message : ""
            }
        })
    }

    const callbackDisconnect = () => {
        // console.log("Internet Disconected");
        setState({
            ...state,
            showToast : true,
            internetConnection : false,
            toastInfo : {
                status : "warning",
                title : "Internet Disconnected",
                message : "Please check your internet connection!"
            }
        })
    }

    const pingGoogle = () => {
        fetch(`/ping/google`)
            .then(response => (response.ok ? callbackConnect() : callbackDisconnect() ))
            .catch(error => console.error("Error: ", error))
      }
  
    useEffect(() => {
    // Check Internet Connection
        setInterval(pingGoogle, 1000);
    }, [state.internetConnection])

    useEffect( () => {
        // fetch("/hello")
        //     .then(response => response.json())
        //     .then(data => setState({
        //         ...state,
        //         message : data.message
        //     }))
        //     .catch(data => console.log(data));

            async function loadHello(){
                try {
                    const response = await fetch("/hello");
                    const data = await response.json();
                    return data;
                } catch (e) {
                    console.error("Error", e);
                }
                
            }
            (async () => {
                try {
                    const data = await loadHello();
                    // console.log(data.message)
                } catch (e) {
                    console.error(e);
                }
            })();

        }, [])

    return (
        <div className="page position-relative">
            <Toast show={state.showToast}
                    onClose={() => setState({
                        ...state,
                        showToast : false
                    })} 
                    className="bg-body-secondary position-fixed front--toast mobile--toast">
                <Toast.Header className={`bg-${state.toastInfo.status}`}>
                    <span className="rounded me-2">💡</span>
                    <strong className="me-auto">
                        {state.toastInfo.title}
                    </strong>
                </Toast.Header>
                <Toast.Body>
                    {state.toastInfo.message}
                </Toast.Body>
            </Toast>
            <Header />
            <Content />
        </div>
    )
}
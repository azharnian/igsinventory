import React, { useEffect, useState } from "react";

import Header from "./Header";
import Content from "./Content"

export default function Page() {
    const [ state, setState ] = useState({
        message : "Hello"
    })

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
                    console.log(data.message)
                } catch (e) {
                    console.error(e);
                }
            })();

        }, [])

    return (
        <div className="page">
            <Header />
            <Content />
        </div>
    )
}
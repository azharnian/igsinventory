import React, { useEffect, useState } from "react";

import Header from "./Header";
import Content from "./Content"

export default function Page() {
    const [ state, setState ] = useState({
        message : "Hello"
    })

    useEffect( () => {
        fetch("/hello")
            .then(response => response.json())
            .then(data => setState({
                ...state,
                message : data.message
            }))
            .catch(data => console.log(data));
        }, [])

    return (
        <div className="page">
            <Header />
            <Content />
        </div>
    )
}
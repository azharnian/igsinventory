import React, { useEffect, useState } from "react";

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
            <h1>{ state.message }</h1>
        </div>
    )
}
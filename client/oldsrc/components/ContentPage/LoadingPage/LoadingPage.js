import React from "react";

import "./LoadingPage.css"
import Logo from "./images/logo.svg"

function LoadingPage(){


    return (
        <div className="loading--page">
            <img src={Logo} />
        </div>
    )
}

export default LoadingPage;
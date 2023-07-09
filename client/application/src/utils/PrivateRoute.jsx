import React, {useContext} from "react";
import { Navigate } from "react-router-dom"
import Page from "../components/Pages/Page";
import AuthContext from "../context/AuthContext";

const PrivateRoute = () => {

    let {statusLogin} = useContext(AuthContext);

    if (statusLogin)
        return (
            <Page />
        )
    return (
        <Navigate to={"/login"} />
    )
}

export default PrivateRoute;
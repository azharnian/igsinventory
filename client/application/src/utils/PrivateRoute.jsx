import React, {useContext} from "react";
import { Navigate } from "react-router-dom"
import Page from "../components/Pages/Page";
import AuthContext from "../context/AuthContext";

const PrivateRoute = () => {

    // let logged = false;
    // console.log("Private Route works!");
    const {user, authTokens} = useContext(AuthContext);
    if (user && authTokens)
        return (
            <Page />
        )
    return (
        <Navigate to={"/login"} />
    )
}

export default PrivateRoute;
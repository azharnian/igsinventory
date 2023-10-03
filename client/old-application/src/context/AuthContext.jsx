import { createContext, useState } from "react";
import { useNavigate } from "react-router-dom";

const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = ({children}) => {

    const navigate = useNavigate();

    let [statusLogin, setStatusLogin] = useState( () =>
                        localStorage.getItem("statusLogin") ? 
                        JSON.parse(localStorage.getItem("statusLogin")) : 
                        null);
    let [user, setUser] = useState( () =>
                        localStorage.getItem("user") ? 
                        JSON.parse(localStorage.getItem("user")) : 
                        null);
    let [authAccessToken, setAuthAccessToken] = useState( () =>
                        localStorage.getItem("access_token") ? 
                        JSON.parse(localStorage.getItem("access_token")) : 
                        null);
    let [authRefreshToken, setAuthRefreshToken] = useState( () =>
                        localStorage.getItem("refresh_token") ? 
                        JSON.parse(localStorage.getItem("refresh_token")) : 
                        null);

    let logoutUser = () => {
        setStatusLogin(false);
        setUser(null);
        setAuthAccessToken(null);
        setAuthRefreshToken(null);
        localStorage.clear();
        navigate("/login");
    }

    let contextData = {
        statusLogin : statusLogin,
        user : user,
        authAccessToken : authAccessToken,
        authRefreshToken : authRefreshToken,
        setStatusLogin : (value) => setStatusLogin(value),
        setUser : (value) => setUser(value),
        setAuthAccessToken : (value) => setAuthAccessToken(value),
        setAuthRefreshToken : (value) => setAuthRefreshToken(value),
        logoutUser : logoutUser
    };
    
    return(
        <AuthContext.Provider value={contextData}>
            {children}
        </AuthContext.Provider>
    )
}
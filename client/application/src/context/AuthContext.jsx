import { createContext, useState } from "react";

const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = ({children}) => {
    let [user, setUser] = useState(null);
    let [authTokens, setAuthTokens] = useState(null);

    let contextData = {
        user : user,
        authTokens : authTokens,
        setUser : (value) => setUser(value),
        setAuthTokens : (value) => setAuthTokens(value)
    };
    
    return(
        <AuthContext.Provider value={contextData}>
            {children}
        </AuthContext.Provider>
    )
}
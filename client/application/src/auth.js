import { createAuthProvider } from "react-token-auth";


export const { useAuth, authFetch, login, logout } = 
    createAuthProvider({
        getAccessToken : "access_token",
        onUpdateToken: token => fetch("/refresh", {
                                    method : "POST",
                                    body : token.refreshToken
                                })
                                .then(response => response.json())
    })
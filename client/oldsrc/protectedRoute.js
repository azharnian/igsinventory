// import React from "react";
// import { useLocation, Navigate, Outlet } from "react-router-dom";
// import { useAuth } from "./auth";

// export default function ProtectedRoute() {

//     const [ logged ] = useAuth();
//     const location = useLocation();

//     return (
//         logged ? <Outlet /> : <Navigate to={`/login`} state={{from : location}} replace/>
//     )
// }

import React from 'react';
import { Route, Navigate } from 'react-router-dom';

const ProtectedRoute = ({ component: Component, isAuthenticated, ...rest }) => (
  <Route
    {...rest}
    render={(props) =>
      isAuthenticated ? (
        <Component {...props} />
      ) : (
        <Navigate to="/login" />
      )
    }
  />
);

export default ProtectedRoute;

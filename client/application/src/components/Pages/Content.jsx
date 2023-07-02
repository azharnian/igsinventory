import React from "react";
import { Link, Outlet } from "react-router-dom";

import "./Page.css"
import 'bootstrap/dist/css/bootstrap.css';


export default function Content(){

    return (
        <div className="container-fluid">
            <div className="row">
                <div className="sidebar border border-right col-md-3 col-lg-2 p-0 bg-body-tertiary">
                    <div className="bg-body-tertiary" tabIndex="-1" id="sidebarMenu" aria-labelledby="sidebarMenuLabel">
                        <div className="d-md-flex flex-column p-0 pt-lg-3 overflow-y-auto">
                            <ul className="nav flex-column">
                                <li className="nav-item">
                                    <Link className="nav-link d-flex align-items-center gap-2 active" aria-current="page" to={`/dashboard`}>
                                        Dashboard
                                    </Link>
                                </li>
                                <li className="nav-item">
                                    <span className="nav-link d-flex align-items-center gap-2 border-bottom">Location</span>
                                    <ul className="nav flex-column ms-4">
                                        <li>
                                            <Link className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                Buildings
                                            </Link>
                                        </li>
                                        <li>
                                            <Link className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                Floors
                                            </Link>
                                        </li>
                                        <li>
                                            <Link className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                Locations
                                            </Link>
                                        </li>
                                    </ul>
                                </li>
                                <li className="nav-item">
                                    <span className="nav-link d-flex align-items-center gap-2 border-bottom">Items</span>
                                    <ul className="nav flex-column ms-4">
                                        <li>
                                            <Link className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/`}>
                                                Search Item
                                            </Link>
                                        </li>
                                        <li>
                                            <Link className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/`}>
                                                List of Items
                                            </Link>
                                        </li>
                                    </ul>
                                </li>
                                <li className="nav-item">
                                    <span className="nav-link d-flex align-items-center gap-2 border-bottom">Activities</span>
                                    <ul className="nav flex-column ms-4">
                                        <li>
                                            <Link className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                Transfer Item
                                            </Link>
                                        </li>
                                        <li>
                                            <Link className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                Update Item
                                            </Link>
                                        </li>
                                    </ul>
                                </li>
                                <li className="nav-item">
                                    <span className="nav-link d-flex align-items-center gap-2 border-bottom">Users</span>
                                    <ul className="nav flex-column ms-4">
                                        <li>
                                            <Link className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                Search User
                                            </Link>
                                        </li>
                                        <li>
                                            <Link className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                User Type
                                            </Link>
                                        </li>
                                        <li>
                                            <Link className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                List of Users
                                            </Link>
                                        </li>
                                    </ul>
                                    
                                </li>
                                <li className="nav-item">
                                    <Link className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/`}>
                                        Logs
                                    </Link>
                                </li>
                            </ul>

                        <h6 className="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-body-secondary text-uppercase">
                            <Link className="link-secondary" to={`/`} aria-label="Add a new report">
                                <span>reports</span>
                            </Link>
                        </h6>
                        <ul className="nav flex-column mb-auto">
                            <li className="nav-item">
                                <Link className="nav-link d-flex align-items-center gap-2" to={`/`}>
                                    Current month
                                </Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link d-flex align-items-center gap-2" to={`/`}>
                                    This Year
                                </Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link d-flex align-items-center gap-2" to={`/`}>
                                    Year-end
                                </Link>
                            </li>
                        </ul>

                        <hr className="my-3" />

                        <ul className="nav flex-column mb-auto">
                            <li className="nav-item">
                                <Link className="nav-link d-flex align-items-center gap-2" to={`/`}>
                                    Sign out
                                </Link>
                            </li>
                        </ul>
                        </div>
                    </div>
                </div>

                <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4 main--content">
                    
                    <Outlet />

                </main>
            </div>
        </div>
    )
}
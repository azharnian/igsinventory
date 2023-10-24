import { useState } from "react";
import { Link, Outlet } from "react-router-dom";
import { Toast } from "react-bootstrap";
import "boxicons"

import Header from "../Miscs/Header";
import Footer from "../Miscs/Footer";

function Content(){

    const [state, setState] = useState({
        clickedLocation : false,
        clickedItems : false,
        clickedActivities : false,
        clickedUsers : false
    })

    const handleClicked = (event) => {
        const name = event.target.getAttribute("name");
        setState({
            ...state,
            [name] : !state[name]
        })
    }

    return (
        <div className="container-fluid">
            <div className="row">
                <div className="sidebar border border-right col-md-3 col-lg-2 p-0 bg-body-tertiary">
                    <div className="bg-body-tertiary" tabIndex="-1" id="sidebarMenu" aria-labelledby="sidebarMenuLabel">
                        <div className="d-md-flex flex-column p-0 pt-lg-3 overflow-y-auto">
                            <ul className="nav flex-column">
                                <li className="nav-item">
                                    <Link role="button" className="nav-link d-flex align-items-center gap-2 active" aria-current="page" to={`/`}>
                                        Dashboard
                                    </Link>
                                </li>
                                <li className="nav-item">
                                    <span role="button"
                                        className="nav-link d-flex align-items-center justify-content-between gap-2 border-bottom"        name="clickedLocation"
                                        onClick={handleClicked}
                                    >
                                        Location
                                        <box-icon type='solid' name='chevron-down'></box-icon>
                                    </span>
                                    
                                    <ul className={`nav flex-column ms-4 ${state.clickedLocation ? "" : "d-none"}`}>
                                        <li>
                                            <Link role="button" className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                Buildings
                                            </Link>
                                        </li>
                                        <li>
                                            <Link role="button" className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                Floors
                                            </Link>
                                        </li>
                                        <li>
                                            <Link role="button" className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                Locations
                                            </Link>
                                        </li>
                                    </ul>
                                </li>
                                <li className="nav-item">
                                    <span role="button"
                                    className="nav-link d-flex align-items-center gap-2 border-bottom justify-content-between"
                                    name="clickedItems"
                                    onClick={handleClicked}
                                    >
                                        Items
                                        <box-icon type='solid' name='chevron-down'></box-icon>
                                    </span>
                                    <ul className={`nav flex-column ms-4 ${state.clickedItems ? "" : "d-none"}`}>
                                        <li>
                                            <Link role="button" className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/`}>
                                                Search Item
                                            </Link>
                                        </li>
                                        <li>
                                            <Link role="button" className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/`}>
                                                List of Items
                                            </Link>
                                        </li>
                                    </ul>
                                </li>
                                <li className="nav-item">
                                    <span role="button"
                                    className="nav-link d-flex align-items-center gap-2 border-bottom justify-content-between"
                                    name="clickedActivities"
                                    onClick={handleClicked}
                                    >
                                        Activities
                                        <box-icon type='solid' name='chevron-down'></box-icon>
                                    </span>
                                    <ul className={`nav flex-column ms-4 ${state.clickedActivities ? "" : "d-none"}`}>
                                        <li>
                                            <Link role="button" className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                Transfer Item
                                            </Link>
                                        </li>
                                        <li>
                                            <Link role="button" className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                Update Item
                                            </Link>
                                        </li>
                                    </ul>
                                </li>
                                <li className="nav-item">
                                    <span role="button"
                                    className="nav-link d-flex align-items-center gap-2 border-bottom justify-content-between"
                                    name="clickedUsers"
                                    onClick={handleClicked}
                                    >
                                        Users
                                        <box-icon type='solid' name='chevron-down'></box-icon>
                                    </span>
                                    <ul className={`nav flex-column ms-4 ${state.clickedUsers ? "" : "d-none"}`}>
                                        <li>
                                            <Link role="button" className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                Search User
                                            </Link>
                                        </li>
                                        <li>
                                            <Link role="button" className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                User Type
                                            </Link>
                                        </li>
                                        <li>
                                            <Link role="button" className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/user-type`}>
                                                List of Users
                                            </Link>
                                        </li>
                                    </ul>
                                    
                                </li>
                                <li className="nav-item">
                                    <Link role="button" className="nav-link d-flex align-items-center gap-2" aria-current="page" to={`/`}>
                                        Logs
                                    </Link>
                                </li>
                            </ul>

                        <h6 className="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-body-secondary text-uppercase">
                            <Link role="button" className="link-secondary" to={`/`} aria-label="Add a new report">
                                <span>reports</span>
                            </Link>
                        </h6>
                        <ul className="nav flex-column mb-auto">
                            <li className="nav-item">
                                <Link role="button" className="nav-link d-flex align-items-center gap-2" to={`/`}>
                                    Current month
                                </Link>
                            </li>
                            <li className="nav-item">
                                <Link role="button" className="nav-link d-flex align-items-center gap-2" to={`/`}>
                                    This Year
                                </Link>
                            </li>
                            <li className="nav-item">
                                <Link role="button" className="nav-link d-flex align-items-center gap-2" to={`/`}>
                                    Year-end
                                </Link>
                            </li>
                        </ul>

                        <hr className="my-3" />

                        <ul className="nav flex-column mb-auto">
                            <li className="nav-item">
                                <p role="button" className="nav-link d-flex align-items-center gap-2 link-item">
                                    Sign out
                                </p>
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

export default function DashboardPage() {

    const [ state, setState ] = useState({
        message : "Hello",
        toastInfo : {
                status : "info",
                title : "Toast Title",
                message : "This is a toast message!"
            },
        showToast : false,
        internetConnection : true
    })

    const callbackConnect = () => {
        setState({
            ...state,
            showToast : false,
            internetConnection : true,
            toastInfo : {
                title : "",
                message : ""
            }
        })
    }

    const callbackDisconnect = () => {
        setState({
            ...state,
            showToast : true,
            internetConnection : false,
            toastInfo : {
                status : "warning",
                title : "Internet Disconnected",
                message : "Please check your internet connection!"
            }
        })
    }

    const pingGoogle = () => {
        fetch(`/ping/google`)
            .then(response => (response.ok ? callbackConnect() : callbackDisconnect() ))
            .catch(error => console.error("Error: ", error))
      }
  
    // useEffect(() => {
    //     setInterval(pingGoogle, 1000);
    // }, [state.internetConnection])

    // useEffect( () => {

    //         async function loadHello(){
    //             try {
    //                 const response = await fetch("/hello");
    //                 const data = await response.json();
    //                 return data;
    //             } catch (e) {
    //                 console.error("Error", e);
    //             }
                
    //         }
    //         (async () => {
    //             try {
    //                 const data = await loadHello();
    //                 // console.log(data.message)
    //             } catch (e) {
    //                 console.error(e);
    //             }
    //         })();

    //     }, [])

    return (
        <div className="page position-relative">
            <Toast show={state.showToast}
                    onClose={() => setState({
                        ...state,
                        showToast : false
                    })} 
                    className="bg-body-secondary position-fixed front--toast mobile--toast">
                <Toast.Header className={`bg-${state.toastInfo.status}`}>
                    <span className="rounded me-2">💡</span>
                    <strong className="me-auto">
                        {state.toastInfo.title}
                    </strong>
                </Toast.Header>
                <Toast.Body>
                    {state.toastInfo.message}
                </Toast.Body>
            </Toast>
            <Header />
            <Content />
            <Footer />
        </div>
    )
}


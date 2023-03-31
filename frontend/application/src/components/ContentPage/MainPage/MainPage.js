import React from 'react'
import './MainPage.css'
import Navigation from '../Navigation/Navigation'
import BuildingEntryForm from '../../Forms/BuildingEntryForm/BuildingEntryForm'
import FloorEntryForm from '../../Forms/FloorEntryForm/FloorEntryForm'
import LocationEntryForm from '../../Forms/LocationEntryForm/LocationEntryForm'
import ItemTypeForm from '../../Forms/ItemTypeForm/ItemTypeForm'

class MainPage extends React.Component {

    render = () => {
        return (
            <div className='container-main-page'>
                <Navigation />
                <div className="container--content--main--page">
                    {/* <h1>OK</h1> */}
                    {/* <BuildingEntryForm /> */}
                    {/* <FloorEntryForm /> */}
                    {/* <LocationEntryForm /> */}
                    <ItemTypeForm />
                </div>
            </div>
        )
    }

}

export default MainPage;
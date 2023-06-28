import React from 'react';
import './Navigation.css';

class ArrowItemList extends React.Component {

    render = () => {
        return (
        <div className='icon-arrow-nav'>
            <box-icon type='solid' name='down-arrow' color='whitesmoke' size='xs'></box-icon>
        </div>
        )
    }

}

class ItemList extends React.Component {

    render = () => {
        return (
            <li onClick={this.props.clickHandler} className={`item-nav ${this.props.hasSubItemList === "true" ? "has-sub-nav" : ""} item-${this.props.title}-nav`}>
                <a className='link-item-nav'>
                    <div className='left'>
                        <box-icon type='solid' name={this.props.icon} color='whitesmoke'></box-icon>
                        <span className='title-item-nav'>{this.props.title}</span>
                    </div>
                    <div className='right'>
                    {this.props.hasSubItemList === "true" ? <ArrowItemList /> : ""}
                    </div>
                    
                </a>
            </li>
        )
    }
}

class Navigation extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            clickedReport : false,
            clickedMaster : false
        }
    }

    componentDidMount = () => {
        const clickedReport = sessionStorage.getItem("clickedReport");
        if (clickedReport !== null){
            this.setState({
                clickedReport : JSON.parse(clickedReport)
            });
        };

        const clickedMaster = sessionStorage.getItem("clickedMaster");
        if (clickedMaster !== null){
            this.setState({
                clickedMaster : JSON.parse(clickedMaster)
            });
        };

        window.addEventListener("beforeunload", () => {
            sessionStorage.setItem("clickedReport", this.state.clickedReport);
            sessionStorage.setItem("clickedMaster", this.state.clickedMaster);
        });
        
    }


    render = () => {
        return (
            <div className='container-nav'>
                <nav>
                    <ul className='list-nav'>
                        <ItemList icon="dashboard" title="dashboard" />
                        <ItemList icon="data" title="database" />

                        <ItemList icon="leaf" title="report" hasSubItemList="true" clickHandler={this.handleReportClicked}/>
                        <ul className={`sub-list-nav ${!this.state.clickedReport ? 'hide-report-sub-list-nav' : ''}`}>
                            <ItemList icon="bowl-rice" title="item" />
                            <ItemList icon="bowl-rice" title="item" />
                            <ItemList icon="bowl-rice" title="item" />
                            <ItemList icon="bowl-rice" title="item" />
                        </ul>
                        <ItemList icon="cat" title="master" hasSubItemList="true" clickHandler={this.handleMasterClicked}/>
                        <ul className={`sub-list-nav ${!this.state.clickedMaster ? 'hide-master-sub-list-nav' : ''}`}>
                            <ItemList icon="bowl-rice" title="item" />
                            <ItemList icon="bowl-rice" title="item" />
                        </ul>
                    </ul>
                </nav>
            </div>
        )
    }

    handleReportClicked = () => {
        this.setState(state => ({
            clickedReport : !state.clickedReport
        }));
    }

    handleMasterClicked = () => {
        this.setState(state => ({
            clickedMaster : !state.clickedMaster
        }));
    }

}

export default Navigation;
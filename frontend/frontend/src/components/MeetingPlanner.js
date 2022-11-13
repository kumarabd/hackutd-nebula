import React, { Component } from "react";
import AddParticipant from './AddParticipant'
import  Planner from './Planner'
import './MeetingPlanner.css'
class MeetingPlanner extends Component {
    

render() {
        return <div className='rowC'>
            <AddParticipant />
            <Planner />
        </div>
    }
}

export default MeetingPlanner;
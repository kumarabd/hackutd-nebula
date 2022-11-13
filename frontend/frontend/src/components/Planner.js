import React, { Component } from "react";
import { ScheduleMeeting } from 'react-schedule-meeting';


class Planner extends Component {
    

    render() {
        
        // const [data, setData] = useState('Empty');
        // const handleTextInputChange = async e => {
        //     const response = await fetch(`http://b41f-129-110-242-17.ngrok.io/api/calender/members`, {
        //             method: 'GET',
        //             crossDomain:true,
        //             headers: {'Content-Type': 'application/json'}
        //           })
        //     const result = await response.json()
        //           console.log(result)
        //           setData(result.data)
 
        //   }
    
        const availableTimeslots = [0, 1, 2, 3, 4, 5].map((id) => {
            return {
            id,
            startTime: new Date(new Date(new Date().setDate(new Date().getDate() + id)).setHours(9, 0, 0, 0)),
            endTime: new Date(new Date(new Date().setDate(new Date().getDate() + id)).setHours(17, 0, 0, 0)),
            };
        });
    
            return (
                <ScheduleMeeting
                    borderRadius={10}
                    primaryColor="#3f5b85"
                    eventDurationInMinutes={15}
                    availableTimeslots={availableTimeslots}
                    onStartTimeSelect={console.log}
                />
            );
        }
    
    
    }
    
    export default Planner;
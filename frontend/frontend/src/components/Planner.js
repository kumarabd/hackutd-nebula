import React, { Component } from "react";
import { ScheduleMeeting } from 'react-schedule-meeting';

class Planner extends Component {

    render() {
        
        //const [data, setData] = useState('Empty');
        let res = []
        let data = []
        const handleTextInputChange = async e => {
            const response = await fetch(`http://127.0.0.1:8081/api/calender/members/{id}`, {
                    method: 'GET',
                    crossDomain:true,
                    headers: {'Content-Type': 'application/json'}
                  })
            const result = await response.json()
                console.log(result)
                data = result.data
                data.forEach(element => {
                for (var key in element) {
                    res.push(element[key])
                }
            });
          }
    
        const availableTimeslots = [0, 1, 2, 3, 4, 5].map((id) => {
            return {
            id,
            startTime: new Date(new Date(new Date().setDate(new Date().getDate() + id)).setHours(9, 0, 0, 0)),
            endTime: new Date(new Date(new Date().setDate(new Date().getDate() + id)).setHours(17, 0, 0, 0)),
            };
        });
    
            return (
                <div>
                    <button style={{marginLeft:'40%'}} onClick={handleTextInputChange}> Get Available Slots </button>
                    <ScheduleMeeting
                    borderRadius={10}
                    primaryColor="#3f5b85"
                    eventDurationInMinutes={15}
                    availableTimeslots={availableTimeslots}
                    onStartTimeSelect={console.log}/>
                </div>
                
            );
        }
    
    
    }
    
    export default Planner;
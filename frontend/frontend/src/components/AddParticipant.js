import React, { Component } from "react";
import 'react-dropdown/style.css';
import './AddParticipant.css'
import TextField from '@material-ui/core/TextField';
import { useState } from "react";
import Autocomplete,
{ createFilterOptions } from '@material-ui/lab/Autocomplete';

const filter = createFilterOptions();

function AddParticipant() {

    const [data,setData] = useState([])
    const [res,setRes] = useState([])
    const [selectedData, setSelectedData] = useState('Empty');
    const handleTextInputChange = async e => {
        if(res.length == 0){
            const response = await fetch(`http://127.0.0.1:8081/api/calender/members`, {
                    method: 'GET',
                    crossDomain:true,
                    headers: {'Content-Type': 'application/json'}
                  })
            const result = await response.json()
            setData(result.data)
            const temp = []
            data.forEach(element => {
                for (const [key, value] of Object.entries(element)) {
                    //console.log(`${key} ${value}`);
                    temp.push(value)
                }
            });
            setRes(temp)
        }
    }
    const handleOnClick = async e => {
        let id = ''
        data.forEach(element => {
            for (const [key, value] of Object.entries(element)) {
                console.log(selectedData)
                if(value == selectedData) {
                    id = key
                    break
                }
            }
        });
        const response = await fetch(`http://127.0.0.1:8081/api/calender/members/${id}`, {
                method: 'GET',
                crossDomain:true,
                headers: {'Content-Type': 'application/json'}
              })
        const result = await response.json()
        console.log(result.data)
    }
    const handleValueChange = async (e,v) => {
        setSelectedData(v)
    }

    return (
        <div style={{ marginLeft: '10px', marginTop: '10px' }}>
          <h3>Add Participant!</h3>
          <Autocomplete
            disablePortal
            options={res}
            id="combo-box-demo"
            style={{ width: 300 }}
            onChange={handleValueChange}
            renderInput={(params) => (
              <TextField {...params} label="Enter Something"
                variant="outlined" value={selectedData} onChange={handleTextInputChange}/>
            )}/>
            <button style={{marginLeft:'40%'}} onClick={handleOnClick}> Get Available Slots </button>
        </div>
        
      );
    }
 
    
export default AddParticipant;
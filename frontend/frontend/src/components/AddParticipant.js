import React, { Component } from "react";
import 'react-dropdown/style.css';
import './AddParticipant.css'
import TextField from '@material-ui/core/TextField';
import { useState } from "react";
import Autocomplete,
{ createFilterOptions } from '@material-ui/lab/Autocomplete';

const filter = createFilterOptions();

function AddParticipant() {

    let data = [];
    let res = [];
    //const [data, setData] = useState('Empty');
    const handleTextInputChange = async e => {
        if(res.length == 0){
            const response = await fetch(`http://127.0.0.1:8081/api/calender/members`, {
                    method: 'GET',
                    crossDomain:true,
                    headers: {'Content-Type': 'application/json'}
                  })
            const result = await response.json()
            data = result.data
            data.forEach(element => {
                for (var key in element) {
                    res.push(element[key])
                }
            });
        }
    }

    

    return (
        <div style={{ marginLeft: '10px', marginTop: '10px' }}>
          <h3>Add Participant!</h3>
          <Autocomplete
            disablePortal
            options={res}
            id="combo-box-demo"
            style={{ width: 300 }}
            renderInput={(params) => (
              <TextField {...params} label="Enter Something"
                variant="outlined" onChange={handleTextInputChange}/>
            )}/>
            </div>
          );
    }
 
    
export default AddParticipant;
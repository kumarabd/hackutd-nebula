import React, { Component } from "react";
import 'react-dropdown/style.css';
import './AddParticipant.css'
import TextField from '@material-ui/core/TextField';
import { useState } from "react";
import Autocomplete,
{ createFilterOptions } from '@material-ui/lab/Autocomplete';

const filter = createFilterOptions();

function AddParticipant() {

    const [data, setData] = useState('Empty');
    const handleTextInputChange = async e => {
    const response = await fetch(`http://127.0.0.1:8081/api/calender/members`, {
                    method: 'GET',
                    crossDomain:true,
                    headers: {'Content-Type': 'application/json'}
                  })
            const result = await response.json()
                  console.log(result)
                  setData(result.data)
    }

    let res = [];
    data.array.forEach(element => {
        for (var key in element) {
            res.push(element[key])
        }
        
    });
    return (
        

        <div style={{ marginLeft: '10px', marginTop: '10px' }}>
          <h3>Add Participant!</h3>
          <Autocomplete
            filterOptions={(data, params) => {
              const filtered = filter(res, params);
              // Suggest the creation of a new value
              if (params.inputValue !== '') {
                filtered.push(`Add "${params.inputValue}"`);
              }
              return filtered;
            }}
            selectOnFocus
            clearOnBlur
            handleHomeEndKeys
            options={data}
            renderOption={(option) => option}
            style={{ width: 300 }}
            freeSolo
            renderInput={(params) => (
              <TextField {...params} label="Enter Something"
                variant="outlined" />
            )}/>
            </div>
          );
    }
 
    
export default AddParticipant;
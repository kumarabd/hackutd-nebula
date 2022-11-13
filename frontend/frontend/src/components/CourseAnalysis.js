import React, { Component, useMemo } from "react";
import 'react-dropdown/style.css';
import './AddParticipant.css'
import TextField from '@material-ui/core/TextField';
import { useState } from "react";
import Autocomplete,
{ createFilterOptions } from '@material-ui/lab/Autocomplete';
import {ScheduleMeeting} from 'react-schedule-meeting';
// import Table from "./Table";
//import ReactTable from "react-table";  

function CourseAnalysis() {

    const [data,setData] = useState([])
    const [res,setRes] = useState([])
    const [selectedSchool, setSelectedSchool] = useState('Empty');

    
    const [selectedMajor, setSelectedMajor] = useState('Empty');

    
    const [selectedTrack, setSelectedTrack] = useState('Empty');

   

    const handleSchoolTextInputChange = async e => {
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

    

    const handleSchoolValueChange = async (e,v) => {
        setSelectedSchool(v)
    }

    const handleMajorValueChange = async (e,v) => {
        setSelectedMajor(v)
    }

    const handleTrackValueChange = async (e,v) => {
        setSelectedTrack(v)
    }

    

    return(
        <div>
        <div style={{ display:'flex' }}>
           <div style={{ marginLeft: '10px', marginTop: '10px' }}>
          <Autocomplete
            disablePortal
            options={res}
            id="combo-box-demo"
            style={{ width: 300 }}
            onChange={handleSchoolValueChange}
            renderInput={(params) => (
              <TextField {...params} label="School"
                variant="outlined" value={selectedSchool} onChange={handleSchoolTextInputChange}/>
            )}/>
             </div>

             <div style={{ marginLeft: '10px', marginTop: '10px' }}>
          <Autocomplete
            disablePortal
            options={res}
            id="combo-box-demo"
            style={{ width: 300 }}
            onChange={handleMajorValueChange}
            renderInput={(params) => (
              <TextField {...params} label="School"
                variant="outlined" value={selectedSchool} onChange={handleSchoolTextInputChange}/>
            )}/>
             </div>

             <div style={{ marginLeft: '10px', marginTop: '10px' }}>
          <Autocomplete
            disablePortal
            options={res}
            id="combo-box-demo"
            style={{ width: 300 }}
            onChange={handleTrackValueChange}
            renderInput={(params) => (
              <TextField {...params} label="School"
                variant="outlined" value={selectedSchool} onChange={handleSchoolTextInputChange}/>
            )}/>
             </div>

             <div style={{ marginLeft: '10px', marginTop: '10px' }}>
          <button>Filter</button>
             </div>
        </div>
{/* table code */}
<div>  
        {/* <ReactTable  
            data={table_data}  
            columns={table_columns}  
            defaultPageSize = {2}  
            pageSizeOptions = {[2,4, 6]}  
         />   */}
     </div>
        </div>
        
    )
    }
 
    
export default CourseAnalysis;
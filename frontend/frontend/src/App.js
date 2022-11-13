//import logo from './logo.svg';
import './App.css';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import MeetingPlanner from './components/MeetingPlanner'
import CourseAnalysis from './components/CourseAnalysis'
import CoursePlanner from './components/CoursePlanner'

function App() {
  //const [tabIndex, setTabIndex] = useState(0);
  //selectedIndex={tabIndex} onSelect={(index) => setTabIndex(index)}
  return (
    <header>
      <Tabs >
      <TabList>
        <Tab>Course Analysis</Tab>
        <Tab>Meeting Scheduler</Tab>
        <Tab>Course Recommendation</Tab>
      </TabList>
      <TabPanel>
        {/* <CourseAnalysis/> */}
      </TabPanel>
      <TabPanel>
        <MeetingPlanner/>
      </TabPanel>
      <TabPanel>
        {/* <CoursePlanner/> */}
      </TabPanel>
    </Tabs>
    </header>
    
  );
}

export default App;

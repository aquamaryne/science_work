import { Button, Typography } from '@mui/material';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import PageThree from './components/pageone';
import MainPage from './components/mainpage';

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path='/mainpage' element={ <MainPage /> } />
          <Route path='/pageone' element={ <PageThree />} />
        </Routes>
        <Button component={Link} to='/pageone'>
            <Typography>Table 3.3</Typography>
        </Button> 
      </Router>

    </div>
  );
}

export default App;

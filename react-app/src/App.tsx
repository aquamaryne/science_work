import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import PageThree from './components/pageone';
import MainPage from './components/mainpage';
import Navbar from './components/navbar';

function App() {
  return (
    <div>
      <Router>
        <Navbar />
        <Routes>
          <Route path='/mainpage' element={ <MainPage /> } />
          <Route path='/pageone' element={ <PageThree />} />
        </Routes>
      </Router>

    </div>
  );
}

export default App;

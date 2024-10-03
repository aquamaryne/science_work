import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import MainPage from './components/mainpage';

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path='/mainpage' element={ <MainPage /> } />
        </Routes>
      </Router>

    </div>
  );
}

export default App;

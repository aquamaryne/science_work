import * as React from 'react';
import { Button, Typography } from '@mui/material';
import { Link } from 'react-router-dom';

const Navbar: React.FC = () => {
    return (
        <div>
            <Button component={Link} to='/mainpage'>
                <Typography>Головна</Typography>
            </Button>
            <Button component={Link} to='/pageone'>
                <Typography>Table 3.3</Typography>
            </Button> 
        </div>
    )
};

export default Navbar;
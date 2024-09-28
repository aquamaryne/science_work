import * as React from 'react';
import { QmzFormData } from '../interface/qmz';
import { QozFormData } from '../interface/qoz';
import Qoz from './qozForm';
import Qmz from './qmzForm';
import { Container, Typography, Paper } from '@mui/material';

const MainPage: React.FC = () => {
    const [qozResult, setQozResult] = React.useState<number | null>(null);
    const [qmzResult, setQmzResult] = React.useState<number | null>(null);

    const handleQozSubmit = async(formData: QozFormData) => {
        const responce = await fetch('http://127.0.0.1:5000/calculate_qoz', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
        });

        const data = await responce.json();
        setQozResult(data.Qoz)
    }

    const handleQmzSubmit = async(formData: QmzFormData) => {
        const responce = await fetch('http://127.0.0.1:5000/calculate_qmz', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
        });

        const data = await responce.json();
        setQmzResult(data.Qmz)
    }

    return (
        <Container maxWidth="sm" sx={{ mt: 4 }}>
            <Typography variant="h4" gutterBottom>
                Calculate QOZ
            </Typography>
            <Qoz onSubmit={handleQozSubmit} />

            {qozResult !== null && (
                <Paper elevation={3} sx={{ p: 2, mt: 2 }}>
                    <Typography variant="h6" color="primary">
                        QOZ Result:
                    </Typography>
                    <Typography variant="body1">{qozResult}</Typography>
                </Paper>
            )}

            <Typography variant="h4" gutterBottom sx={{ mt: 4 }}>
                Calculate QMZ
            </Typography>
            <Qmz onSubmit={handleQmzSubmit} />

            {qmzResult !== null && (
                <Paper elevation={3} sx={{ p: 2, mt: 2 }}>
                    <Typography variant="h6" color="secondary">
                        QMZ Result:
                    </Typography>
                    <Typography variant="body1">{qmzResult}</Typography>
                </Paper>
            )}
        </Container>
    );
}

export default MainPage;
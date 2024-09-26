import React, { FormEvent } from "react";
import { QozFormData, QozFormProps } from "../interface/qoz";
import { TextField, Button, Box, Typography } from "@mui/material";

const Qoz: React.FC<QozFormProps> = ({ onSubmit }) => {
    const[formData, setFormData] = React.useState<QozFormData>({
        Q1: 0,
        Qt: 0,
        Qmizh: 0,
        Qias: 0,
        Qlits: 0,
        Qn: 0,
        Qvp: 0,
        Qup: 0,
        Qdpp: 0,
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFormData({
            ...formData,
            [e.target.name]: parseFloat(e.target.value),
        });
    };

    const handleSubmit = (e: FormEvent) => {
        e.preventDefault();
        onSubmit(formData);
    };

    return(
        <Box
            component="form"
            onSubmit={handleSubmit}
            sx={{
                display: "flex",
                flexDirection: "column",
                gap: 2,
                maxWidth: 400,
                margin: "0 auto",
                padding: 2,
                backgroundColor: "#f5f5f5",
                borderRadius: 2,
                boxShadow: 3,
            }}
        >
            <Typography variant="h5" align="center" gutterBottom>
                Qmz Form
            </Typography>
        
            <Box
                sx={{
                    display: "flex",
                    flexWrap: "wrap",
                    justifyContent: "center",
                    gap: 2,
                    maxWidth: "100%",
                }}
            >
                <TextField
                    label="Q1"
                    name="Q1"
                    type="number"
                    value={formData.Q1}
                    onChange={handleChange}
                    fullWidth
                    variant="outlined"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                <TextField
                    label="Qt"
                    name="Qt"
                    type="number"
                    value={formData.Qt}
                    onChange={handleChange}
                    fullWidth
                    variant="outlined"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                <TextField
                    label="Qmizh"
                    name="Qmizh"
                    type="number"
                    value={formData.Qmizh}
                    onChange={handleChange}
                    fullWidth
                    variant="outlined"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                <TextField
                    label="QIAS"
                    name="Qias"
                    type="number"
                    value={formData.Qias}
                    onChange={handleChange}
                    fullWidth
                    variant="outlined"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                <TextField
                    label="Qlits"
                    name="Qlits"
                    type="number"
                    value={formData.Qlits}
                    onChange={handleChange}
                    fullWidth
                    variant="outlined"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                <TextField
                    label="Qn"
                    name="Qn"
                    type="number"
                    value={formData.Qn}
                    onChange={handleChange}
                    fullWidth
                    variant="outlined"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                <TextField
                    label="Qvp"
                    name="Qvp"
                    type="number"
                    value={formData.Qvp}
                    onChange={handleChange}
                    fullWidth
                    variant="outlined"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                <TextField
                    label="Qup"
                    name="Qup"
                    type="number"
                    value={formData.Qup}
                    onChange={handleChange}
                    fullWidth
                    variant="outlined"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                <TextField
                    label="QDPP"
                    name="Qdpp"
                    type="number"
                    value={formData.Qdpp}
                    onChange={handleChange}
                    fullWidth
                    variant="outlined"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                </Box>

            <Button type="submit" variant="contained" color="primary" fullWidth>
                Calculate
            </Button>
        </Box>
    )
}

export default Qoz;
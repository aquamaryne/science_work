import React, { FormEvent } from "react";
import { QmzFormProps, QmzFormData } from "../interface/qmz";
import { TextField, Button, Box, Typography } from "@mui/material";

const Qmz: React.FC<QmzFormProps> = ({ onSubmit }) => {
    const[formData, setFormData] = React.useState<QmzFormData>({
        Q2: 0,
        Qkred: 0,
        Qias2: 0,
        Qn2: 0,
        Qdpp2: 0,
        Qkom: 0,
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
                maxWidth: "100%",
                margin: "0 auto",
                padding: 2,
                backgroundColor: "#f5f5f5",
                borderRadius: 2,
                boxShadow: 3,
            }}
        >
            <Typography variant="h5" align="center" gutterBottom>
                Qmz Calculation Form
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
                    label="Q2"
                    name="Q2"
                    type="number"
                    value={formData.Q2}
                    onChange={handleChange}
                    fullWidth
                    variant="standard"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                <TextField
                    label="Qkred"
                    name="Qkred"
                    type="number"
                    value={formData.Qkred}
                    onChange={handleChange}
                    fullWidth
                    variant="standard"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                <TextField
                    label="Qias2"
                    name="Qias2"
                    type="number"
                    value={formData.Qias2}
                    onChange={handleChange}
                    fullWidth
                    variant="standard"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                <TextField
                    label="Qn2"
                    name="Qn2"
                    type="number"
                    value={formData.Qn2}
                    onChange={handleChange}
                    fullWidth
                    variant="standard"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                <TextField
                    label="Qdpp2"
                    name="Qdpp2"
                    type="number"
                    value={formData.Qdpp2}
                    onChange={handleChange}
                    fullWidth
                    variant="standard"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
                <TextField
                    label="Qkom"
                    name="Qkom"
                    type="number"
                    value={formData.Qkom}
                    onChange={handleChange}
                    fullWidth
                    variant="standard"
                    sx={{ flexBasis: 'calc(25% - 16px)', minWidth: 120 }}
                />
            </Box>

            <Button type="submit" variant="contained" color="primary" fullWidth>
                Calculate
            </Button>
        </Box>
    )
}

export default Qmz;
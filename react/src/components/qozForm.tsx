import React, { FormEvent } from "react";
import { QozFormData, QozFormProps } from "../interface/qoz";

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
        <form onSubmit={handleSubmit}>
            <input name="Q1" value={formData.Q1} onChange={handleChange} />
            <input name="Qt" value={formData.Qt} onChange={handleChange} />
            <input name="Qmizh" value={formData.Qmizh} onChange={handleChange} />
            <input name="QIAS" value={formData.Qias} onChange={handleChange} />
            <input name="Qlits" value={formData.Qlits} onChange={handleChange} />
            <input name="Qn" value={formData.Qn} onChange={handleChange} />
            <input name="Qvp" value={formData.Qvp} onChange={handleChange} />
            <input name="Qup" value={formData.Qup} onChange={handleChange} />
            <input name="QDPP" value={formData.Qdpp} onChange={handleChange} />
            <button type="submit">Calculate</button>
        </form>
    )
}

export default Qoz;
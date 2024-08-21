import React, { FormEvent } from "react";
import { QmzFormData, QmzFormProps } from "../interface/qmz";

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
        <form onSubmit={handleSubmit}>
            <input name="Q2" value={formData.Q2} onChange={handleChange} />
            <input name="Qkred" value={formData.Qkred} onChange={handleChange} />
            <input name="Qias2" value={formData.Qias2} onChange={handleChange} />
            <input name="Qn2" value={formData.Qn2} onChange={handleChange} />
            <input name="Qdpp2" value={formData.Qdpp2} onChange={handleChange} />
            <input name="Qkom" value={formData.Qkom} onChange={handleChange} />
            <button type="submit">Calculate</button>
        </form>
    )
}

export default Qmz;
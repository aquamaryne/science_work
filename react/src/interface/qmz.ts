export interface QmzFormData{
    Q2: number,
    Qkred: number,
    Qias2: number,
    Qn2: number,
    Qdpp2: number,
    Qkom: number,
}

export interface QmzFormProps{
    onSubmit: (formData: QmzFormData) => void;
}
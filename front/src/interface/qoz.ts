export interface QozFormData{
    Q1: number,
    Qt: number,
    Qmizh: number,
    Qias: number,
    Qlits: number,
    Qn: number,
    Qvp: number,
    Qup: number,
    Qdpp: number,
}

export interface QozFormProps{
    onSubmit: (formData: QozFormData) => void;
}
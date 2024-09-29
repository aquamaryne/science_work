import * as React from "react";
import axios from "axios";
import { Typography, Select, MenuItem, SelectChangeEvent } from '@mui/material';

interface RoadLevel {
    'Рівень вимог': string,
    'Значення автомобільної дороги загального користування': string;
    'Інтенсивність руху в транспортних одиницях, авт./добу': string;
    'Опис рівня'?: string;
}

const PageThree: React.FC = () => {
    const [data, setData] = React.useState<RoadLevel[]>([]);
    const [selectedLevel, setSelectedLevel] = React.useState<string>('');
    const [description, setDescription] = React.useState<string>('');
    const [roadValue, setRoadValue] = React.useState<string>('');

    React.useEffect(() => {
        axios.get<RoadLevel[]>('http://127.0.0.1:5000/road_levels')
        .then((responce) => {
            setData(responce.data);
        })
        .catch((error) => {
            console.error('Error fetching data: ', error);
        });
    }, []);

    const handleSelectChange = (event: SelectChangeEvent<string>) => {
        const selected = event.target.value as string | undefined;
        if(typeof selected === 'string'){
            setSelectedLevel(selected);

            const selectedData = data.find(item => item['Інтенсивність руху в транспортних одиницях, авт./добу'] === selected);
            if(selectedData){
                setDescription(selectedData['Опис рівня'] || '');
                setRoadValue(selectedData['Значення автомобільної дороги загального користування'] || '');
            } else {
                setDescription('');
            }
        }

    };

    return (
        <div>
            <Select value={selectedLevel} onChange={handleSelectChange} displayEmpty>
                <MenuItem value="">
                    <em> -- Виберіть інтенсивність руху -- </em>
                </MenuItem>
                {data.map ((item) => (
                    <MenuItem key={item['Інтенсивність руху в транспортних одиницях, авт./добу']} value={item['Інтенсивність руху в транспортних одиницях, авт./добу']}>
                        {item['Інтенсивність руху в транспортних одиницях, авт./добу']}
                    </MenuItem>
                ))}
            </Select>
            {roadValue && (
                <Typography variant="body1" style={{ marginTop: '10px' }}>
                    {roadValue}
                </Typography>
            )}
        </div>
    )
}
export default PageThree;
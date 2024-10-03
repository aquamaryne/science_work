import * as React from 'react';
import { Box, Typography, MenuItem, Select, FormControl, InputLabel, SelectChangeEvent } from "@mui/material";
import city from '../interface/city';
interface City {
    id: number,
    name: string,
};

const cities: City[] = [
    { id: 1, name: 'Вінницька область' },
    { id: 2, name: 'Волинська область' },
    { id: 3, name: 'Дніпропетровська область' },
    { id: 4, name: 'Донецька область' },
    { id: 5, name: 'Житомирська область' }, 
    { id: 6, name: 'Закарпатська область' },
    { id: 7, name: 'Запорізька область' },
    { id: 8, name: 'Івано-Франківська область' },
    { id: 9, name: 'Київська область' },
    { id: 10, name: 'Кіровоградська область' },
    { id: 11, name: 'Луганська область' },
    { id: 12, name: 'Львівська область' },
    { id: 13, name: 'Миколаївська область' },
    { id: 14, name: 'Одеська область' },
    { id: 15, name: 'Полтавська область' },
    { id: 16, name: 'Рівненська область' },
    { id: 17, name: 'Сумська область' },
    { id: 18, name: 'Тернопільська область' },
    { id: 19, name: 'Харківська область' },
    { id: 20, name: 'Херсонська область' },
    { id: 21, name: 'Хмельницька область' },
    { id: 22, name: 'Черкаська область' },
    { id: 23, name: 'Чернігівська область' },
    { id: 24, name: 'Чернівецька область' },
    { id: 25, name: 'Автономна Республіка Крим' },
];

const MainPage: React.FC = () => {
    const [selectedById, setSelectedById] = React.useState<number | null>(null);

    const handleCityChange = (e: SelectChangeEvent<string | number>) => {
        const cityId = Number(e.target.value);
        setSelectedById(cityId);
    };

    return (
        <Box sx={{ maxWidth: 400, margin: '0 auto', padding: 2 }}>
            <FormControl fullWidth variant='standard' sx={{ marginBottom: 2 }}>
                <InputLabel>Оберіть область</InputLabel>
                <Select
                    value={selectedById || ''}
                    onChange={handleCityChange}
                    label='Оберіть область'
                >
                    {cities.map((city) => (
                        <MenuItem key={city.id} value={city.id}>
                            {city.name}
                        </MenuItem>
                    ))}
                </Select>
            </FormControl>
            {selectedById !== null && (
                <Box>
                    <Typography variant='h6'></Typography>
                    <Typography>{city[selectedById]}</Typography>
                </Box>
            )}
        </Box>
    );
}

export default MainPage;
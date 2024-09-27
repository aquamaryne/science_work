import * as React from "react";
import { Typography, FormControl, Select, MenuItem, Box, SelectChangeEvent } from '@mui/material';

interface RoadLevel {
    'Рівень вимог': string,
    'Значення автомобільної дороги загального користування': string;
    'Інтенсивність руху в транспортних одиницях, авт./добу': string;
    'Опис рівня'?: string;
}

const PageThree: React.FC = () => {
    const [levels, setLevels] = React.useState<RoadLevel[]>([]);
    const [selectedLevel, setSelectedLevel] = React.useState<RoadLevel | null>(null);
    const [description, setDesription] = React.useState<string>('');

    React.useEffect(() => {
        fetch('/road_levels')
            .then((responce) => responce.json())
            .then((data: RoadLevel[]) => setLevels(data))
            .catch((error) => console.error('Error while uploading data', error));
    }, []);

    const handleSelectChange = (event: SelectChangeEvent<string>) => {
        const value = event.target.value;
        const level = levels.find((lvl) => lvl['Рівень вимог'] === value);
        setSelectedLevel(level || null);
        setDesription(level ? level['Опис рівня'] || 'Немає опису для цього рівня' : '');
    }

    return (
        <Box p={2}>
            <Typography variant="h4" gutterBottom>
                Оберіть рівень доріг
            </Typography>
            <FormControl fullWidth variant='outlined'>
                <Select
                    value={selectedLevel ? selectedLevel['Рівень вимог'] : ''}
                    onChange={handleSelectChange}
                    displayEmpty
                >
                    <MenuItem value="">
                        <em> -- Рівень доріг -- </em>
                    </MenuItem>
                    {levels.map((level, index) => (
                        <MenuItem key={index} value={level['Рівень вимог']}>
                            Рівень {level['Рівень вимог']}
                        </MenuItem>
                    ))}
                </Select>
            </FormControl>

            {selectedLevel && (
                <Box mt={2}>
                    <Typography variant="h5">Пояснення</Typography>
                    <Typography>{description}</Typography>
                    <Typography>
                        Інтенсивність: { selectedLevel['Інтенсивність руху в транспортних одиницях, авт./добу']}
                    </Typography>
                </Box>
            )}
        </Box>    
    );
}

export default PageThree;
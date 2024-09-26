import * as React from "react";

interface RoadLevel {
    'Рівень вимог': string,
    'Значення автомобільної дороги загального користування': string;
    'Інтенсивність руху в транспортних одиницях, авт./добу': string;
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

    const handleSelectChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
        const selected = levels.find(level => level['Рівень вимог'] === event.target.value) || null;
        setSelectedLevel(selected);
        setDesription(selected ? selected['Значення автомобільної дороги загального користування'] : '');
    }

    return (
        <div>
            <h1>Оберіть рівень доріг</h1>
            <select onChange={handleSelectChange}>
                <option value=""> -- Рівень доріг -- </option>
                {levels.map((level, index) => (
                    <option key={index} value={level['Рівень вимог']}>
                        Рівень {level['Рівень вимог']}
                    </option>
                ))}
            </select>

            {selectedLevel && (
                <div>
                    <h2>Пояснення</h2>
                    <p>{description}</p>
                    <p>Інтенсивність: {selectedLevel['Інтенсивність руху в транспортних одиницях, авт./добу']}</p>
                </div>
            )}
        </div>
    )
}

export default PageThree;
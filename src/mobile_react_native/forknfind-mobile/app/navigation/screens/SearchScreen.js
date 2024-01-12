/* 
-----------------
Reference: https://www.youtube.com/watch?v=Q4S9M9rJAxk&ab_channel=PradipDebnath
           - This video was used as a reference for the search functionality (not the filtering of the search)
           https://www.youtube.com/watch?v=YwwX0DiAvCQ&ab_channel=CodewithBeto
           - This video was used as a reference for the filtering of the search, adapting it to my own code
-----------------
*/

import * as React from 'react';
import { View, Text, StyleSheet, Pressable, TextInput, ActivityIndicator, FlatList, Image } from 'react-native';

const API_ENDPOINT = 'https://randomuser.me/api/?results=30'; // TODO: Add own API endpoint

export default function SearchScreen({ navigation }) {

    const [isLoading, setIsLoading] = React.useState(false);
    const [data, setData] = React.useState([]);
    const [error, setError] = React.useState(null);
    const [fullData, setFullData] = React.useState([]);
    const [searchQuery, setSearchQuery] = React.useState('');

    React.useEffect(() => {
        setIsLoading(true);
        fetchData(API_ENDPOINT)
    }, []);

    const fetchData = async(url) => { // Fetching data and handling errors
        try {
            const response = await fetch(url);
            const json = await response.json();
            setData(json.results);

            console.log(json.results);

        } catch (error) {
            setError(error);
            console.log(error);
        } finally {
            setIsLoading(false);
        }
    }

    const handleSearch = (query) => { // This is the function that handles the search and its filtering
        setSearchQuery(
            data.filter((item) => 
                item.name.first.toUpperCase().includes(query.toUpperCase()) || item.name.last.toUpperCase().includes(query.toUpperCase())
            
        ));
        console.log(query);
    }

    if (isLoading) { // The loading screen/animation
        return (
            <View style= {{ flex: 1, alignItems: 'center', justifyItems: 'center' }}>
                <ActivityIndicator size='large' color='#5500dc' />
            </View>
        );
    }

    if (error) { // Error handling
        console.log(error);
        return (
            <View style={{ flex: 1, alignItems: 'center', justifyItems: 'center' }}>
                <Text style= {{ fontSize: 26, fontWeight: 'bold' }}>Error fetching data...</Text>
            </View>
        )
    }

    return (
        <View style={{ flex: 1, marginHorizontal: 20}}>
            <TextInput 
            placeholder="Search" 
            clearButtonMode='always'
            style={styles.searchBox}
            autoCapitalize='none'
            autoCorrect={false}
            value={searchQuery}
            onChangeText={(query) => handleSearch(query)}
            />
            <FlatList
            data={searchQuery}
            keyExtractor={(item) => item.login.username}
            renderItem={({item}) => (
                <View style={styles.itemContainer}>
                    <Image source={{uri: item.picture.thumbnail}} style={styles.image}/>
                    <View>
                        <Text style={styles.textName}>{item.name.first} {item.name.last}</Text>
                        <Text style={styles.textEmail}>{item.email}</Text>
                    </View>
                </View>
            )}/>
        </View>
    );
}

const styles = StyleSheet.create ({
    searchBox: {
        paddingHorizontal: 20,
        paddingVertical: 10,
        marginTop: 10,
        borderColor: '#ccc',
        borderWidth: 1,
        borderRadius: 8
    },
    itemContainer: {
        flexDirection: 'row',
        alignItems: 'center',
        marginLeft: 10,
        marginTop: 10,
    },
    image: {
        width: 50,
        height: 50,
        borderRadius: 25,
    },
    textName: {
        fontSize: 17,
        marginLeft: 10,
        fontWeight: '600',
    },
    textEmail: {
        fontSize: 14,
        marginLeft: 10,
        color: 'grey',
    }
})
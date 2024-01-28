import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, FlatList } from 'react-native';
import { TextInput } from 'react-native-gesture-handler';
import GetAllCategoriesAPIRequest from '../requests/GetAllCategoriesAPIRequest';

/* 
-----------------
Reference: https://www.youtube.com/watch?v=Q4S9M9rJAxk&ab_channel=PradipDebnath
           - This video was used as a reference for the search functionality (not the filtering of the search)
           https://www.youtube.com/watch?v=YwwX0DiAvCQ&ab_channel=CodewithBeto
           - This video was used as a reference for the filtering of the search, adapting it to my own code
-----------------
*/

// Functional Component CategoryFilter
// selectedCategories - categories selected by user
// setSelectedCategories - setting those categories
const CategoryFilter = ({selectedCategories, setSelectedCategories}) => {

    // Use states of all the possible changes
    const [searchQuery, setSearchQuery] = useState('');
    const [itemList, setItemList] = useState([]);

    // Get all categories via API
    useEffect(() => {
        GetAllCategoriesAPIRequest(setItemList);
    }, []);

    // Search function, filters the search results based on query
    const handleSearch = (query) => {
        // when query is blank show now categories
        if (query == "") {
            setSearchQuery([])
            return 
        }
        setSearchQuery(
            itemList.filter((item) =>  {
                return item.toUpperCase().includes(query.toUpperCase());
            })
        );
    }

    // Add categories to the list
    const addToSearch = (item) => {
        if (!selectedCategories.includes(item)) {
            setSelectedCategories([...selectedCategories, item])
        }

    }

    // remove categories from the list
    const removeFromSearch = (item) => {
        if (selectedCategories.includes(item)) {
            setSelectedCategories((prevList) => prevList.filter((word) => word !== item))
        }
    }

    return (
        <View style={[styles.textContainer]}>
            <Text style={styles.ratingHeadingText}>Categories</Text>
            <TextInput 
                placeholder="Categories"
                placeholderTextColor="black"
                autoCapitalize='none'
                style={styles.textBox}
                autoCorrect={false}
                value={searchQuery}
                onChangeText={(query) => handleSearch(query)}
                >
            </TextInput>
            {/* Flatlist displaying all the information returned from search */}
            <FlatList
            data={searchQuery.slice(0, 6)}
            style={styles.flatListStyle}
            scrollEnabled={false}
            keyExtractor={(item, index) => index.toString()}
            renderItem={({item}) => (
                <TouchableOpacity key={item} onPress={() => addToSearch(item)}>
                    <View style={styles.flatListButton}>
                        <Text style={styles.flatListItem}>{item}</Text>
                    </View>
                </TouchableOpacity>
            )}/>
            <View style={[styles.priceLevelDivisor]}>
                {/* Display all the currently selected categories to user */}
                {selectedCategories.map((category, index) => (
                <TouchableOpacity key={index} onPress={() => removeFromSearch(category)}>
                    <View style={[styles.typeBox, {marginRight: '3%', marginBottom: '4%'}]} >
                        <Text style={styles.typeText}>{category}</Text>
                    </View>
                </TouchableOpacity>
                ))}
            </View>
        </View>
    );
}

const styles = StyleSheet.create({

    // Text container for the search query
    textContainer: {
        paddingTop: '4%',
        paddingLeft: '10%',
        paddingRight: '10%',
        backgroundColor: 'white',
        paddingBottom: '4%',
    },
    // Headings for category
    ratingHeadingText: {
        fontWeight: '700',
        fontSize: 16,
        color: '#525357',
    },
    // text box for styling input text
    textBox: {
        color: 'black',
        paddingHorizontal: 20,
        paddingVertical: 8,
        marginTop: 12,
        borderRadius: 18,
        fontSize: 16,
        fontWeight: '500',
        borderWidth: 3,
        borderColor: "#525357",
    }, 
    // styling of flat list
    flatListStyle: {
        padding: '2%',
    }, 
    // styling of item being returned in flat list 
    flatListItem: {
        paddingTop: '2%',
        fontSize: 16,
        fontWeight: '500',
    },
    // flex direction to keep in a line
    priceLevelDivisor: {
        flexDirection: 'row',
        flexWrap: 'wrap'
    },
    // box for categories selected
    typeBox: {
        paddingLeft: 7,
        paddingRight: 7,
        paddingBottom: 2,
        paddingTop: 1,
        borderRadius: 50,
        backgroundColor: 'rgba(28, 88, 242, 0.20)',
        borderWidth: 3,
        borderColor: "#1C58F2",
        alignItems: 'flex-start',
        alignSelf: 'flex-start',
    },
    // text styling
    typeText: {
        fontSize: 16,
        color: '#333333',
        fontWeight: '600',
    },
})

export default CategoryFilter
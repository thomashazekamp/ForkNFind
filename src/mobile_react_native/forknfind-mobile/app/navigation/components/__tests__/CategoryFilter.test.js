import React from 'react';
import { render } from '@testing-library/react-native';
import CategoryFilter from '../CategoryFilter';

describe('CategoryFilter', () => {
    // mock categories
    const mockCategories = ['testChinese', 'testIndian', 'testItalian'];

    it('renders Categories text', () => {
        const { getByText } = render(<CategoryFilter selectedCategories={mockCategories}/>);
        expect(getByText('Categories')).toBeTruthy();
    });
});
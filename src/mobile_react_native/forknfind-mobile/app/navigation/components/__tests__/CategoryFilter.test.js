import React from 'react';
import { render, waitFor } from '@testing-library/react-native';
import CategoryFilter from '../CategoryFilter';

describe('CategoryFilter', () => {
    // mock categories
    const mockCategories = ['testChinese', 'testIndian', 'testItalian'];

    it('renders Categories text', async () => {
        const { getByText, findByText } = render(<CategoryFilter selectedCategories={mockCategories}/>);
        await waitFor(() => getByText('Categories'), {timeout: 30000});
        await findByText('Categories');
        expect(getByText('Categories')).toBeTruthy();
    });

    it('Should create a snapshot', () => {
        const tree = render(<CategoryFilter selectedCategories={mockCategories}/>).toJSON();
        expect(tree).toMatchSnapshot();
    });
});
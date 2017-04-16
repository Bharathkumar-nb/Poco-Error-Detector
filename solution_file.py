def predictor( row ):
	m_mode = 'Yes'
	h_mode = '1'
	grad = row['Education']  # no empties
	area = row['Property_Area']  # no empties
	married = row['Married'] if row['Married'] != '' else m_mode
	history = row['Credit_History'] if row['Credit_History'] != '' else h_mode
	
	if grad == 'Graduate':
		if history == 1:
			return 'Y'
		else:
			return 'N'
	else:
		if area != 'Rural':
			if married == 'Yes':
				return 'Y'
			else:
				return 'N'
		else:
			return 'N'
	ret_val = None
	if 'Graduate' == grad:
		if 1 == history:
			ret_val = 'Y'
		else:
			ret_val = 'N'
	else:
		if area != 'Rural':
			if married == 'Yes':
				ret_val = 'Y'
			else:
				ret_val = 'N'
		else:
			ret_val = 'N'
	return ret_val
def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    m_total= int(input('Enter the number of MALE students registered in your class: '))
    f_total = int(input('Enter the number of FEMALE students registered in your class: '))
    classtotal = m_total + f_total
    m_perc = m_total/classtotal
    f_perc = f_total/classtotal
    print (f'The number of MALE students in your class is \t {m_total:4d}')
    print (f'The number of FEMALE students in your class is \t {f_total:4d}')
    print (f'The TOTAL number of students in your class is \t {classtotal:4d}')
    print()
    print (f'The percent of your class that is MALE is \t {m_perc:.2f}')
    print (f'The percent of your class that is FEMALE is \t {f_perc:.2f}')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()

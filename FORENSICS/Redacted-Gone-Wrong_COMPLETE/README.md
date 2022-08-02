# Redacted-Gone-Wrong

## FLAG: picoCTF{C4n_Y0u_S33_m3_fully}

## Status: Complete

Category: Forensics

Description: Now you DON’T see me. This report has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?

## STEPS

1. wget <https://artifacts.picoctf.net/c/264/Financial_Report_for_ABC_Labs.pdf>
2. Copy all text from PDF
3. Paste text
   1. This should ideally copy all the text ommiting the correctly redacted text but leaving behind the incorrectly redacted text.

    ```text
        Financial Report for ABC Labs, Kigali, Rwanda for the year 2021. Breakdown - Just painted over in MS word.
        Cost Benefit Analysis
        Credit Debit
        This is not the flag, keep looking Expenses from the picoCTF{C4n_Y0u_S33_m3_fully} Redacted document.
    ```

4. In the text we have the flag: `picoCTF{C4n_Y0u_S33_m3_fully}`

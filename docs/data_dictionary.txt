providerCcn (oscarNumber)
Data Type: String
Alpha-numeric 6-13 character provider number. Also known as Oscar Number.

effectiveDate
Data Type: String
Must be numeric, CCYYMMDD. This is the effective date of the provider's first PPS period, or for subsequent PPS periods, the effective date of a change to the PROV file. If a termination date is present for this record, the effective date must be equal to or less than the termination date. Year: Greater than 82, but not greater than current year. Month: 01-12 Day: 01-31.

fiscalYearBeginDate (fiscalYearBeginningDate)
Data Type: String
Must be updated annually to show the current year for providers receiving a blended payment based on their FY begin date. Must be equal to or less than the effective date.

exportDate (reportDate)
Data Type: String
Must be numeric, CCYYMMDD. Date file created/run date of the PROV report for submittal to CMS CO.

terminationDate
Data Type: String
Termination Date in this context is the date on which the reporting MAC ceased servicing the provider. Must be zeroes or contain a termination date. Must be equal to or greater than the effective date. If the provider is terminated or transferred to another MAC, a termination date is placed in the file to reflect the last date the provider was serviced by the outgoing MAC.

waiverIndicator
Data Type: String
Y = waived (Provider is not under PPS).
N = not waived (Provider is under PPS).

intermediaryNumber
Data Type: String
Assigned intermediary number of the Medicare Administrative Contractor (MAC).

providerType
Data Type: String
This identifies the inpatient provider type, such as short term facility, long-term, psychiatric, rehabilitation facility, and so on.

censusDivision
Data Type: String
The Census division to which the facility belongs for payment purposes. When a facility is reclassified for the standardized amount, MACs must change the census division to reflect the new standardized amount location.

msaActualGeographicLocation (actualGeographicLocation_MSA)
Data Type: String
Enter the appropriate code for the MSA 0040-9965, or the rural area, (blank) (blank) 2 digit numeric State code such as _ _36 for Ohio, where the facility is physically located.

msaWageIndexLocation (wageIndexLocation_MSA)
Data Type: String
Enter the appropriate code for the MSA, 0040-9965, or the rural area, (blank) (blank) (2 digit numeric State code) such as _ _ 3 6 for Ohio, to which a hospital has been reclassified due to its prevailing wage rates. Leave blank or enter the actual location MSA (field 13), if not reclassified. Pricer will automatically default to the actual location MSA if this field is left blank.

msaStandardizedAmountLocation (standardizedAmountLocation_MSA)
Data Type: String
Enter the appropriate code for the MSA, 0040-9965, or the rural area, (blank) (blank) (2 digit numeric State code) such as _ _ 3 6 for Ohio, to which a hospital has been reclassified for standardized amount. Leave blank or enter the actual location MSA (field 13) if not reclassified. Pricer will automatically default to the actual location MSA if this field is left blank.

soleCommunityOrMedicareDependentHospitalBaseYear
Data Type: String
Leave blank if not a sole community hospital (SCH) or a Medicare dependent hospital (MDH) effective with cost reporting periods that begin on or after April 1, 1990. If an SCH or an MDH, show the base year for the operating hospital specific rate, the higher of either 82 or 87. See §20.6. Must be completed for any SCH or MDH that operated in 82 or 87, even if the hospital will be paid at the Federal rate. Eff. 10/1/12, MDHs are no longer valid provider types.

changeCodeForLugarReclassification
Data Type: String
Will contain an "L" if the MSA has been reclassified for wage index purposes under §1886(d)(8)(B) of the Act. These are also known as Lugar reclassifications, and apply to ASC-approved services provided on an outpatient basis when a hospital qualifies for payment under an alternate wage index MSA. Leave blank for hospitals if there has not been a Lugar reclassification.

temporaryReliefIndicator
Data Type: String
Enter a “Y” if this provider qualifies for a payment update under the temporary relief provision, otherwise leave blank.

federalPpsBlend
Data Type: String
HH PPS: For “From” dates before 1/1/2021: the value to indicate if normal percentage payments should be made on RAP and/or whether payment should be reduced under the Quality Reporting Program. Valid values: 0 = Make normal percentage payment; 1 = Pay 0%; 2 = Make final payment reduced by 2%; 3 = Make final payment reduced by 2%. pay RAPs at 0%

stateCode (state)
Data Type: String
Enter the 2-digit state where the provider is located. Enter only the first (lowest) code for a given state. For example, effective October 1, 2005, Florida has the following State Codes: 10, 68 and 69. MACs shall enter a “10” for Florida’s state code.List of valid state codes is located in Pub. 100-07, Chapter 2, Section 2779A1.

caseMixAdjustedCostPerDischarge_PpsFacilitySpecificRate
Data Type: Number
For PPS hospitals and waiver state non-excluded hospitals, the base year cost per discharge divided by the case mix index. Will have zero for new providers.

costOfLivingAdjustment
Data Type: Number
The COLA adjustment. All hospitals except Alaska and Hawaii use 1.000.

internsToBedsRatio
Data Type: Number
This is the provider's intern/resident to bed ratio. Calculated by dividing the provider's full time equivalent residents by the number of available beds. Enter zero for non-teaching hospitals.

bedSize
Data Type: Number
Enter the number of adult hospital beds and pediatric beds available for lodging inpatient. Must be greater than zero.

operatingCostToChargeRatio
Data Type: Number
Derived by MACs from the latest settled cost report and corresponding charge data from the billing file. Computed amount by dividing the Medicare operating costs by Medicare covered charges.

caseMixIndex
Data Type: Number
The case mix index is used to compute positions field 18. Zero-fill for all others.

supplementalSecurityIncomeRatio
Data Type: Number
The SSI ratio used to determine if the hospital qualifies for a disproportionate share adjustment and to determine the size of the capital and operating DSH adjustments.

medicaidRatio
Data Type: Number
The Medicaid ratio used to determine if the hospital qualifies for a disproportionate share adjustment and to determine the size of the capital and operating DSH adjustments.

specialProviderUpdateFactor
Data Type: Number
Zero-fill for all hospitals after FY91. This Field is obsolete for hospitals as of FY92. Effective 1/1/2018, this field is used for HHAs only. Enter the HH VBP adjustment factor provided by CMS for each HHA. If no factor is provided, enter 1.00000.

operatingDsh
Data Type: Number
Disproportionate share adjustment Percentage. Pricer calculates the Operating DSH effective 10/1/91 and bypasses this field. Zero-fill for all hospitals 10/1/91 and later.

fiscalYearEndDate (fiscalYearEnd)
Data Type: String
This field is no longer used. If present, must be CCYYMMDD.

specialPaymentIndicator
Data Type: String
The code that indicates the type of special payment provision that applies.
Blank = not applicable
Y = reclassified
1 = special wage index indicator
2 = both special wage index indicator and reclassified
D = Dual reclassified

hospitalQualityIndicator
Data Type: String
Code to indicate that hospital meets criteria to receive higher payment per MMA quality standards. Blank = hospital does not meet criteria' 1 = hospital quality standards have been met

cbsaActualGeographicLocation (actualGeographicLocation_CBSA)
Data Type: String
Enter the appropriate code for the CBSA 00001-89999, or the rural area, (blank (blank) (blank) 2 digit numeric State code such as _ _ _ 36 for Ohio, where the facility is physically located.

cbsaWageIndexLocation (wageIndexLocation_CBSA)
Data Type: String
Enter the appropriate code for the CBSA, 00001-89999, or the rural area, (blank)(blank) (blank) (2 digit numeric State code) such as _ _ _ 3 6 for Ohio, to which a hospital has been reclassified due to its prevailing wage rates. Leave blank or enter the actual location CBSA (field 35), if not reclassified. Pricer will automatically default to the actual location CBSA if this field is left blank.

cbsaStandardizedAmountLocation (standardizedAmountLocation_CBSA)
Data Type: String
The appropriate code for the CBSA, 00001-89999 or the rural area, (blank) (blank)(blank) (2 digit numeric State code) such as _ _ _ 3 6 for Ohio, to which a hospital has been reclassified. Leave blank or enter the actual location CBSA (31) if not reclassified. Pricer will automatically default to the actual location CBSA if this field is left blank.

specialWageIndex
Data Type: Number
Enter the special wage index that certain providers may be assigned. Enter zeroes unless the Special Payment Indicator field equals a “1” or “2.”

passThroughAmountForCapital
Data Type: Number
Per diem amount based on the interim payments to the hospital. Zero-fill if this does not apply.

passThroughAmountForDirectMedicalEducation
Data Type: Number
Per diem amount based on the interim payments to the hospital Zerofill if this does not apply.

passThroughAmountForOrganAcquisition
Data Type: Number
Per diem amount based on the interim payments to the hospital. Zerofill if this does not apply.

passThroughTotalAmount (totalPassThroughAmount)
Data Type: Number
Per diem amount based on the interim payments to the hospital. Zerofill if this does not apply.

capitalPpsPaymentCode
Data Type: String
Enter the code to indicate the type of capital payment methodology for hospitals: A = Hold Harmless – cost payment for old capital; B = Hold Harmless – 100% Federal rate; C = Fully prospective blended rate.

hospitalSpecificCapitalRate
Data Type: Number
Must be present unless: • A "Y" is entered in the Capital Indirect Medical Education Ratio field; or
A“08” is entered in the Provider Type field; or
A termination date is present in Termination Date field.
Enter the hospital's allowable adjusted base year inpatient capital costs per discharge.
This field is not used as of 10/1/02.

oldCapitalHoldHarmlessRate
Data Type: Number
Enter the hospital's allowable inpatient "old" capital costs per discharge incurred for assets acquired before December 31, 1990, for capital PPS. Update annually.

newCapitalHoldHarmlessRate
Data Type: Number
Enter the ratio of the hospital's allowable inpatient costs for new capital to the hospital's total allowable inpatient capital costs. Update annually.

capitalCostToChargeRatio
Data Type: Number
Derived from the latest cost report and corresponding charge data from the billing file. For hospitals for which the MAC is unable to compute a reasonable cost-to-charge ratio, it uses the appropriate statewide average cost-to-charge ratio calculated annually by CMS and published in the "Federal Register."

newHospital
Data Type: String
Enter "Y" for the first 2 years that a new hospital is in operation. Leave blank if hospital is not within first 2 years of operation.

capitalIndirectMedicalEducationRatio
Data Type: Number
This is for IPPS hospitals and IRFs only. Enter the ratio of residents/interns to the hospital's average daily census. Calculate by dividing the hospital's full-time equivalent total of residents during the fiscal year by the hospital's total inpatient days. Zero-fill for a non-teaching hospital.

capitalExceptionPaymentRate
Data Type: Number
The per discharge exception payment to which a hospital is entitled.

vpbParticipantIndicator (valueBasedPurchasingParticipant)
Data Type: String
Enter “Y” if participating in Hospital Value Based Purchasing. Enter “N” if not participating. Note if Data Element AD (Hospital Quality Ind) is blank, then this field must = N.

vbpAdjustment (valueBasedPurchasingAdjustment)
Data Type: Number
Enter VBP Adjustment Factor. If prior element (vpbParticipantIndicator) is blank, leave blank.

hhrParticipantIndicator (hospitalReadmissionsReductionProgramParticipant)
Data Type: Number
Enter “0” if not participating in Hospital Re-admissions Reduction program.
Enter “1” if participating in Hospital Re-admissions Reduction program and payment adjustment is not 1.0000.
Enter “2” if participating in Hospital Re-admissions Reduction program and payment adjustment is equal to 1.0000.

hhrAdjustment (hospitalReadmissionsReductionAdjustment)
Data Type: Number
Enter HRR Adjustment Factor if “1” is entered in prior element (hhrParticipantIndicator). Leave blank if “0” or “2” is entered in AW Participant indicator.

bundleModel1Discount
Data Type: Number
The discount % for hospitals participating in Bundled Payments for Care Improvement Initiative (BPCI), Model 1 (demo code 61).

hacReductionParticipantIndicator (hospitalAcquiredConditionReductionProgramParticipant)
Data Type: String
Enter a ‘Y’ if the hospital is subject to a reduction under the HAC Reduction Program. Enter a ‘N’ if the hospital is NOT subject to a reduction under the HAC Reduction Program.

uncompensatedCareAmount
Data Type: Number
Enter the estimated per discharge uncompensated care payment amount calculated and published by CMS for each hospital.

ehrReductionIndicator (electronicHealthRecordsProgramReduction)
Data Type: String
Enter a ‘Y’ if the hospital is subject to a reduction due to NOT being an EHR meaningful user. Leave blank if the hospital is an Electronic Health Records meaningful user.

lowVolumeAdjustmentFactor
Data Type: Number
Enter the low-volume hospital payment adjustment factor calculated and published by the Centers for Medicare & Medicaid Services (CMS) for each eligible hospital.

countyCode
Data Type: String
Enter the County Code. Must be 5 numbers.

medicarePerformanceAdjustment
Data Type: Number
Enter the MPA percentage calculated and published by the Centers for Medicare & Medicaid Services (CMS).

ltchDppIndicator
Data Type: String
Enter a ‘Y’ if the LTCH is subject to the DPP payment adjustment. Leave blank if the LTCH is not subject to the DPP payment adjustment.

supplementalWageIndex
Data Type: Number
Enter the supplemental wage index that certain providers may be assigned. Enter zeroes if it does not apply.

supplementalWageIndexIndicator (supplementalWageIndexFlag)
Data Type: String
Enter the supplemental wage index indicator that certain providers may be assigned: 1=Prior Year Wage Index*; 2=Future use; 3=Future use; Enter blank if it does not apply
Note: For LTCH’s providers this is the IPPS prior year wage index.

changeCodeWageIndexReclassification
Data Type: String
Enter "Y" if hospital's wage index location has been reclassified for the year. Enter "N" if it has not been reclassified for the year. Adjust annually.

nationalProviderIdentifier
Data Type: String
Alpha-numeric 10 character NPI number.

passThroughAmountForAllogenicStemCellAcquisition
Data Type: Number
The per diem payment amount based on the interim payments to the hospital that includes acquisition amounts for allogeneic stem cell. The pass-through amount is not included in total pass-through and miscellaneous field.

ppsBlendYearIndicator
Data Type: String
The year where there is a blend of payments from cost-based principles and the Federal Long Term Care Hospital (LTCH) PPS rate.

lastUpdated
Data Type: String
A date formatted as an ISO 8601 date string (YYYY-MM-DD), specifying the date that the provider record was last updated in the VSAM PSF file. This date is inclusive.

passThroughAmountForDirectGraduateMedicalEducation
Data Type: Number
Per diem amount of direct graduate medical education to be excluded from Medicare Advantage (MA) capitation rates per regulation.

passThroughAmountForKidneyAcquisition
Data Type: Number
Per diem amount of kidney acquisition costs to be excluded from MA capitation rates per regulation.

passThroughAmountForSupplyChain
Data Type: Number
Per diem amount of Supply Chain Cost to be excluded from Medicare Advantage (MA) capitation rates per regulation.
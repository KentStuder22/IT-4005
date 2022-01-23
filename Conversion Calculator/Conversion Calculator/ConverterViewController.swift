//
//  CalculatorViewController.swift
//  Conversion Calculator
//
//  Created by Kent Studer on 3/24/21.
//

import UIKit

class ConverterViewController: UIViewController{
    @IBOutlet weak var outputDisplay: UITextField!
    @IBOutlet weak var inputDisplay: UITextField!
    
    var conversion = [Convert(label: "fahrenheit to celcius", inUnit: "°F", outUnit: "°C"),
                      Convert(label: "celcius to fahrenheit", inUnit: "°C", outUnit: "°F"),
                      Convert(label: "miles to kilometers", inUnit: "mi", outUnit: "km"),
                      Convert(label: "kilometers to miles", inUnit: "km", outUnit: "mi")]

    override func viewDidLoad() {
        super.viewDidLoad()
        outputDisplay.text = conversion[0].outUnit
        inputDisplay.text = conversion[0].inUnit
    }
    var input = ""
    @IBAction func converterAction(_ sender: Any) {
        let alert = UIAlertController(title: "", message: "Choose Converter", preferredStyle: UIAlertController.Style.actionSheet)
        alert.addAction(UIAlertAction(title: conversion[0].label, style: UIAlertAction.Style.default, handler: { [self]
            (AlertAction) -> Void in
            self.input += self.conversion[0].inUnit
            if(outputDisplay.text?.count == 2){
                self.outputDisplay.text = self.conversion[0].outUnit
            }else{
                self.outputDisplay.text = (convertValue(input: inputDisplay.text!).dropLast(2)) + self.conversion[0].outUnit
            }
            self.inputDisplay.text = inputDisplay.text!.dropLast(2) + self.conversion[0].inUnit
        }))
        alert.addAction(UIAlertAction(title: conversion[1].label, style: UIAlertAction.Style.default, handler: { [self]
            (AlertAction) -> Void in
            if(outputDisplay.text?.count == 2){
                self.outputDisplay.text = self.conversion[1].outUnit
            }else{
                self.outputDisplay.text = (convertValue(input: inputDisplay.text!).dropLast(2)) + self.conversion[1].outUnit
            }
            self.inputDisplay.text = inputDisplay.text!.dropLast(2) + self.conversion[1].inUnit
        }))
        alert.addAction(UIAlertAction(title: conversion[2].label, style: UIAlertAction.Style.default, handler: { [self]
            (AlertAction) -> Void in
            if(outputDisplay.text?.count == 2){
                self.outputDisplay.text = self.conversion[2].outUnit
            }else{
                self.outputDisplay.text = (convertValue(input: inputDisplay.text!).dropLast(2)) + self.conversion[2].outUnit
            }
            self.inputDisplay.text = inputDisplay.text!.dropLast(2) + self.conversion[2].inUnit
        }))
        alert.addAction(UIAlertAction(title: conversion[3].label, style: UIAlertAction.Style.default, handler: { [self]
            (AlertAction) -> Void in
            if(outputDisplay.text?.count == 2){
                self.outputDisplay.text = self.conversion[3].outUnit
            }else{
                self.outputDisplay.text = (convertValue(input: inputDisplay.text!).dropLast(2)) + self.conversion[3].outUnit
            }
            self.inputDisplay.text = inputDisplay.text!.dropLast(2) + self.conversion[3].inUnit
        }))
        self.present(alert, animated: true, completion: nil)
        }
    
    @IBAction func Button0(_ sender: Any) {
        inputDisplay.text?.insert("0", at: inputDisplay.text!.index(inputDisplay.text!.endIndex, offsetBy: -2))
        displayResult(input: inputDisplay.text!)
    }
    @IBAction func ButtonDec(_ sender: Any) {
        inputDisplay.text?.insert(".", at: inputDisplay.text!.index(inputDisplay.text!.endIndex, offsetBy: -2))
        displayResult(input: inputDisplay.text!)
    }
    @IBAction func Button1(_ sender: Any) {
        inputDisplay.text?.insert("1", at: inputDisplay.text!.index(inputDisplay.text!.endIndex, offsetBy: -2))
        displayResult(input: inputDisplay.text!)
    }
    @IBAction func Button2(_ sender: Any) {
        inputDisplay.text?.insert("2", at: inputDisplay.text!.index(inputDisplay.text!.endIndex, offsetBy: -2))
        displayResult(input: inputDisplay.text!)
    }
    @IBAction func Button3(_ sender: Any) {
        inputDisplay.text?.insert("3", at: inputDisplay.text!.index(inputDisplay.text!.endIndex, offsetBy: -2))
        displayResult(input: inputDisplay.text!)
    }
    @IBAction func Button4(_ sender: Any) {
        inputDisplay.text?.insert("4", at: inputDisplay.text!.index(inputDisplay.text!.endIndex, offsetBy: -2))
        displayResult(input: inputDisplay.text!)
    }
    @IBAction func Button5(_ sender: Any) {
        inputDisplay.text?.insert("5", at: inputDisplay.text!.index(inputDisplay.text!.endIndex, offsetBy: -2))
        displayResult(input: inputDisplay.text!)
    }
    @IBAction func Button6(_ sender: Any) {
        inputDisplay.text?.insert("6", at: inputDisplay.text!.index(inputDisplay.text!.endIndex, offsetBy: -2))
        displayResult(input: inputDisplay.text!)
    }
    @IBAction func Button7(_ sender: Any) {
        inputDisplay.text?.insert("7", at: inputDisplay.text!.index(inputDisplay.text!.endIndex, offsetBy: -2))
        displayResult(input: inputDisplay.text!)
    }
    @IBAction func Button8(_ sender: Any) {
        inputDisplay.text?.insert("8", at: inputDisplay.text!.index(inputDisplay.text!.endIndex, offsetBy: -2))
        displayResult(input: inputDisplay.text!)
    }
    @IBAction func Button9(_ sender: Any) {
        inputDisplay.text?.insert("9", at: inputDisplay.text!.index(inputDisplay.text!.endIndex, offsetBy: -2))
        displayResult(input: inputDisplay.text!)
    }
    @IBAction func ButtonClear(_ sender: Any) {
        let inCount = inputDisplay.text?.count
        let outCount = outputDisplay.text?.count
        
        inputDisplay.text?.removeFirst(inCount! - 2)
        outputDisplay.text?.removeFirst(outCount! - 2)
    }
    func displayResult(input: String){
        let converted = convertValue(input: input)
        
        outputDisplay.text = converted
    }
    
    func convertValue(input: String) -> String{
        let inUnit = inputDisplay.text?.last
        let outUnit = outputDisplay.text?.last
        let outerUnits = outputDisplay.text?.suffix(2)
        
        let inString = inputDisplay.text?.dropLast(2)
        let inValue = Float(inString!)
        var converted: Float = 0
        
        if(inUnit == "F" && outUnit == "C"){
            converted = ((inValue! - 32) * (5/9))
        }
        else if(inUnit == "C" && outUnit == "F"){
            converted = ((inValue! * (9/5)) + 32)
        }
        else if(inUnit == "i" && outUnit == "m"){
            converted = (inValue! * 1.609)
        }
        else if(inUnit == "m" && outUnit == "i"){
            converted = (inValue! / 1.609)
        }
        let finalConvert = String(converted) + outerUnits!
        return finalConvert
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}

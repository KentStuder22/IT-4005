//
//  SingleExpViewController.swift
//  Expenses
//
//  Created by Kent Studer on 4/7/21.
//

import UIKit

class SingleExpViewController: UIViewController {
    @IBOutlet weak var nameField: UITextField!
    @IBOutlet weak var amountField: UITextField!
    @IBOutlet weak var dateField: UIDatePicker!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        nameField.delegate = self
        amountField.delegate = self
        // Do any additional setup after loading the view.
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        nameField.resignFirstResponder()
        amountField.resignFirstResponder()
    }

    @IBAction func saveExpense(_ sender: Any) {
        let name = nameField.text
        let amountText = amountField.text ?? ""
        let amount = Double(amountText) ?? 0.0
        let date = dateField.date
        
        if let expense = Expense(name: name, amount: amount, date: date) {
            do {
                let managedContext = expense.managedObjectContext
                
                try managedContext?.save()
                
                self.navigationController?.popViewController(animated: true)
            } catch {
                print("Expense could not be saved")
            }
        }
    }
}
extension SingleExpViewController: UITextFieldDelegate {
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }
}
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */



//
//  HelloWorldViewController.swift
//  Hello World
//
//  Created by Kent Studer on 2/10/21.
//

import UIKit

class HelloWorldViewController: UIViewController {
    @IBOutlet weak var displayLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    @IBAction func doHello(_ sender: UIButton) {
        displayLabel.text = "Hello World!"
    }
    
    @IBAction func doClear(_ sender: UIButton) {
        displayLabel.text = ""
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

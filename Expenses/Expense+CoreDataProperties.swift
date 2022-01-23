//
//  Expense+CoreDataProperties.swift
//  Expenses
//
//  Created by Kent Studer on 4/7/21.
//
//

import Foundation
import CoreData


extension Expense {

    @nonobjc public class func fetchRequest() -> NSFetchRequest<Expense> {
        return NSFetchRequest<Expense>(entityName: "Expense")
    }

    @NSManaged public var name: String?
    @NSManaged public var amount: Double
    @NSManaged public var rawDate: NSDate?

}

extension Expense : Identifiable {

}

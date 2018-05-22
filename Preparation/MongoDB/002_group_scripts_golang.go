	//db.events.aggregate([{ "$group": { "_id": { "userid": "$userid", "yearMonthDayUTC": { $dateToString: { format: "%Y-%m-%d", date: "$dateCreate" } }}, "count": { "$sum": 1 } } }])
	var group = bson.M{
		"$group" : bson.M{
			"_id": bson.M{"userid": "$userid",
			"yearMonthDayUTC": bson.M{"$dateToString": bson.M{
					"format": "%Y-%m-%d", "date": "$dateCreate" }}},
			"count": bson.M{ "$sum": 1 },
		},
	}
